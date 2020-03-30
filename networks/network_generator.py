class Network:
    def __init__(self):
        pass

    def get_dag(self, name):
        if name == 'asia':
            from networks import get_dag_asia
            return get_dag_asia
        elif name == 'galaxy':
            from networks import get_dag_galaxy
            return get_dag_galaxy
        elif name == 'inversetree':
            from networks import get_dag_inversetree
            return get_dag_inversetree
        elif name == 'rain':
            from networks import get_dag_rain
            return get_dag_rain
        else:
            raise RuntimeError()
