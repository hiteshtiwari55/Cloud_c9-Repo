import pytest
import pandas as pd
# sample Test
def test_order():
    print("After Conftest")
    print(pd.__version__)
    df = pd.DataFrame(range(0, 5))
    print("Hello!! Git crash course!!")
    print("Hello!! First Branch Commit!!!Git crash course!!")
    print(df)