
def circle(radius:float) -> None:
    area =3.14 * radius * radius
    print(f"Area of Circle with radius {radius} = {area}") 


def rectangle(length :float , breadth :float) -> None:
    area =length* breadth
    print(f"Area of rectangle with  = {area}") 


def traingle(base:float, height: float) -> None:
    area =0.5 * base * height
    print(f"Area of triangle = {area}") 


if __name__=="___main__":

    circle(0.45)
    rectangle(34,29)