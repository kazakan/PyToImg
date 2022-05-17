# PyToImg

Just make .py to png file. That's all.

## Example

Let's make python file `./codes_to_cvt/fibonacci.py` with under code to png file.

``` python
def fibonacci(n):
    a, b = 0, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a
```

In bash, type

``` bash
python ./src/main.py -t dt2 -n 1
```

Result is

![fibonacci_dt2](/docs/imgs/fibonacci_dt2.png)

When option `t` is `text` you get below image.

![fibonacci_justtext](/docs/imgs/fibonacci_justtext.png)

When `t` = `matrix` you get this.

![fibonacci_matrix](/docs/imgs/fibonacci_matrix.png)
