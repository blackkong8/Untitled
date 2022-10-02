import pytermgui as ptg


with ptg.YamlLoader() as loader, open("pytermgui/examples/common.yaml", "r") as config:
    namespace = loader.load(config)


with ptg.WindowManager() as manager:
    window = ptg.Window("Nasdaq")
    namespace.apply_to(window)
    manager += window