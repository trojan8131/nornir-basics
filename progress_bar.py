from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
import time
from tqdm import tqdm

nr = InitNornir(config_file="config.yaml")


def multiple_progress_bar(task, napalm_get_bar, other_bar):
    task.run(task=napalm_get, getters=["facts"])
    time.sleep(3)
    napalm_get_bar.update()
    tqdm.write(f"{task.host}: facts gathered")
    other_bar.update()
    tqdm.write(f"{task.host}: done!")


with tqdm(
    total=len(nr.inventory.hosts), desc="gathering facts",
) as napalm_get_bar:
    with tqdm(
        total=len(nr.inventory.hosts), desc="other action   ",
    ) as other_bar:
        nr.run(
            task=multiple_progress_bar,
            napalm_get_bar=napalm_get_bar,
            other_bar=other_bar,
        )