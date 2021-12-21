from invidious_api_client import get_instances



def test_instances():
    for instance in get_instances().instances:
        print(f"{instance.uri} ({instance.region}, {f'{instance.monitor.month_ratio.ratio} % uptime in the last month' if instance.monitor else '[no monitor data]'}")



if __name__ == "__main__":
    test_instances()
