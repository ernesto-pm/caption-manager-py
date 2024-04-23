from dependency_injector.wiring import Provide, inject
from src.containers import Container

@inject
def main():
    pass

if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])