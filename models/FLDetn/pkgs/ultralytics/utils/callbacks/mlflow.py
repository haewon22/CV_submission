# Ultralytics YOLO 🚀, AGPL-3.0 license

from models.FLDetn.pkgs.ultralytics.utils import LOGGER, SETTINGS, TESTS_RUNNING, colorstr

try:
    assert not TESTS_RUNNING  # do not log pytest
    assert SETTINGS['mlflow'] is True  # verify integration is enabled
    import mlflow

    assert hasattr(mlflow, '__version__')  # verify package is not directory
    PREFIX = colorstr('MLFlow:')
    import os
    import re

except (ImportError, AssertionError):
    mlflow = None


def on_pretrain_routine_end(trainer):
    """Logs training parameters to MLflow."""
    global mlflow, run, experiment_name

    if os.environ.get('MLFLOW_TRACKING_URI') is None:
        mlflow = None

    if mlflow:
        mlflow_location = os.environ['MLFLOW_TRACKING_URI']  # "http://192.168.xxx.xxx:5000"
        LOGGER.debug(f'{PREFIX} tracking uri: {mlflow_location}')
        mlflow.set_tracking_uri(mlflow_location)
        experiment_name = os.environ.get('MLFLOW_EXPERIMENT_NAME') or trainer.args.project or '/Shared/YOLOv8'
        run_name = os.environ.get('MLFLOW_RUN') or trainer.args.name
        experiment = mlflow.set_experiment(experiment_name)  # change since mlflow does this now by default

        mlflow.autolog()
        prefix = colorstr('MLFlow: ')
        try:
            run, active_run = mlflow, mlflow.active_run()
            if not active_run:
                active_run = mlflow.start_run(experiment_id=experiment.experiment_id, run_name=run_name)
            LOGGER.info(f'{prefix}Using run_id({active_run.info.run_id}) at {mlflow_location}')
            run.log_params(vars(trainer.model.args))
        except Exception as err:
            LOGGER.error(f'{prefix}Failing init - {repr(err)}')
            LOGGER.warning(f'{prefix}Continuing without Mlflow')


def on_fit_epoch_end(trainer):
    """Logs training metrics to Mlflow."""
    if mlflow:
        metrics_dict = {f"{re.sub('[()]', '', k)}": float(v) for k, v in trainer.metrics.items()}
        run.log_metrics(metrics=metrics_dict, step=trainer.epoch)


def on_train_end(trainer):
    """Called at end of train loop to log model artifact info."""
    if mlflow:
        run.log_artifact(trainer.last)
        run.log_artifact(trainer.best)
        run.log_artifact(trainer.save_dir)
        mlflow.end_run()
        LOGGER.debug(f'{PREFIX} ending run')


callbacks = {
    'on_pretrain_routine_end': on_pretrain_routine_end,
    'on_fit_epoch_end': on_fit_epoch_end,
    'on_train_end': on_train_end} if mlflow else {}
