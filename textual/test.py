from textual.app import App
from textual.widgets import Placeholder


class SimpleApp(App):

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(name="hi1"), Placeholder(name="hi2"), edge="left", size=20)
        await self.view.dock(Placeholder(), Placeholder(), Placeholder(), edge="top")


SimpleApp.run(log="textual.log")