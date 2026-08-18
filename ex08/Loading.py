import os

# width:
#   (total terminal width) - 5(100%|) -
#   (| (333)/(333) ) -
#   26([00:01<00:00, 177.24it/s](\n))
# fsting:
# \r            : carriage return, move cursor back to beginning line
# :3            : minimum width, ex: '  5' ' 50' '100'
# :<20          : left aligned width 20
# end=""        : no '\n'
# flush=True    : output imidiatly


# like original with ███
def ft_tqdm(lst: range) -> None:
    ''' Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progress bar every time a value is requested.

    Returns
    -------
    out  : decorated iterator. '''
    total = len(lst)
    width = os.get_terminal_size().columns - 5 - \
        (4 + (2 * len(str(total)))) - 26
    for i, elem in enumerate(lst, 1):
        p = i * 100 // total
        bar = "█" * (p * width // 100)
        print(f"\r{p:3}%|{bar:<{width}}| {i}/{total}", end="", flush=True)
        yield elem


# like example with [==>] width - 3 ([>])
# def ft_tqdm(lst: range) -> None:
#   total = len(lst)
#   width = os.get_terminal_size().columns - 5 - \
#       (4 + (2 * len(str(total)))) - 26 - 3
#   for i, elem in enumerate(lst, 1):
#       p = i * 100 // total
#       bar = "=" * (p * width // 100)
#       print(f"\r{p:3}%|[{bar + '>':<{width}}]| {i}/{total}", \
#           end="", flush=True)
#       yield elem
