def diff(first_d: dict, second_d: dict) -> dict:
    result = {}
    keys = sorted(first_d.keys() | second_d.keys())

    for key in keys:
        if isinstance(first_d.get(key, ''), dict) and isinstance(
                second_d.get(key, ''), dict):
            result[f'  {key}'] = diff(first_d.get(key),
                                      second_d.get(key))

        elif key in first_d and key in second_d:
            if first_d.get(key) == second_d.get(key):
                result[f'  {key}'] = first_d.get(key)
            else:
                result[f'- {key}'] = first_d.get(key)
                result[f'+ {key}'] = second_d.get(key)

        elif key in first_d:
            result[f'- {key}'] = first_d.get(key)
        elif key in second_d:
            result[f'+ {key}'] = second_d.get(key)
    return result
