def feet_to_steps(feet):
    return (int)(feet / 2.5)

if __name__ == '__main__':
    input_feet = float(input())
    steps = feet_to_steps(input_feet)
    print(steps)