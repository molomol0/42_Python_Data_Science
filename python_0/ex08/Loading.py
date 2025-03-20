def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for x, y in enumerate(lst):
        current = int((1 + x) * 100 / total)
        print(f"\r{current}%|[" + "=" * current + " " * (100 - current) + "]|"
              + str(x + 1) + "/" + str(total), end='')
        yield y
