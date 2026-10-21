"""FizzBuzz minimal — script de validation de la chaîne Linus -> Composio -> GitHub."""


def fizzbuzz(n):
    """Retourne la suite FizzBuzz de 1 à n sous forme de liste.

    Chaque élément est soit "Fizz" (multiple de 3), "Buzz" (multiple de 5),
    "FizzBuzz" (multiple de 15), soit le nombre lui-même sous forme de str.

    Args:
        n: borne supérieure incluse. n < 1 retourne une liste vide.

    Returns:
        list[str]
    """
    if n < 1:
        return []

    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


if __name__ == "__main__":
    print(fizzbuzz(15))
