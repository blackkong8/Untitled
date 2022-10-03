from ctypes import alignment
from textual.app import App
from textual import events

from textual.widget import Widget
from textual.widgets import Placeholder

from textual.reactive import Reactive

from datetime import datetime

from rich.align import Align


class Clock(Widget):

    mouse_over = Reactive(False)
    mouse_click = Reactive(False)

    def on_mount(self):
        self.set_interval(1, self.refresh)

    def render(self):
        time = datetime.now().strftime("%c")
        if self.mouse_click:
            return Align.center("Click!")
        else:
            return Align.center(f"Time is {time}", vertical="middle", style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
    
    async def on_mouse_down(self, event: events.MouseDown) -> None:
        self.mouse_click = True
        return await super().on_mouse_down(event)
    
    async def on_mouse_up(self, event: events.MouseUp) -> None:
        self.mouse_click = False
        return await super().on_mouse_up(event)


class SimpleApp(App):

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(name="hi1"), Placeholder(name="hi2"), edge="left", size=20)
        await self.view.dock(Placeholder(), Placeholder(), Placeholder(), Clock(), edge="top")


SimpleApp.run(log="textual.log")
