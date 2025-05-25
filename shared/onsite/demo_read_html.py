import pandas


def read_table(url: str) -> list:
    return pandas.read_html(url)


if __name__ == "__main__":
    print(
            read_table(
                'https://simple.wikipedia.org/wiki/List_of_U.S._states'
        )[0].head(6)
    )
