from src.app.app import App

def test_sum():
    app = App()
    assert app.sum(2, 2) == 4
