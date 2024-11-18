import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    """Access both function sin and function tan in terminal with smallangle
    """    
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of points function sin generates.",
    show_default=True,  # show default in help
)
def sin(number):
    """Get a list of points between 0 and 2pi and their sinus
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Number of points function tan generates.",
    show_default=True,  # show default in help
)
def tan(number):
    """Get a list of points between 0 and 2pi and their tangent
    """  
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()