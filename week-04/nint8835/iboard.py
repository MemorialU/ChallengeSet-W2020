print(
    (
        lambda _, __, ___: (
            lambda ____, _____: _____.whitespace[___].join(
                [
                    frozenset.__name__[:___] + eval.__name__[_] + eval.__name__[_]
                    if ______.count(str(__)) % ___ == _
                    and ______.count(str(_)) % ___ == _
                    else str.__name__[__:]
                    + map.__name__[__:]
                    + type.__name__[___:]
                    + dir.__name__[_]
                    for ______ in [
                        str().join(
                            [
                                bin(ord(________))[___:].zfill(___ * ___ * ___ - __)
                                for ________ in _______.strip()
                            ]
                        )
                        for _______ in ____.stdin.readlines()
                    ]
                ]
            )
        )(
            __import__(str.__name__[_] + type.__name__[__] + str.__name__[_]),
            __import__(str.__name__ + int.__name__[: _ - __] + globals.__name__[_]),
        )
    )(*map(len, [[], [...], [..., ...]]))
)
