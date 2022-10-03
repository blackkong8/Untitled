from textual.app import App
from textual.widget import Widget
from textual.widgets import Placeholder

from datetime import datetime

from rich.align import Align


class Clock(Widget):
    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        time = datetime.now().strftime("%c")
        return Align.center(time, vertical="middle")


class SimpleApp(App):

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(name="hi1"), Placeholder(name="hi2"), edge="left", size=20)
        await self.view.dock(Placeholder(), Placeholder(), Placeholder(), Clock(), edge="top")


SimpleApp.run(log="textual.log")
