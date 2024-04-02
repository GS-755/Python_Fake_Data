class FormatExportString:
  def execute(text, arrays) -> str:
    item_count = len(arrays)
    if(item_count == 0):
      return f'{text}[]'
    result = f'{text} [\n'
    count = 0
    for item in arrays:
      count += 1
      if(count == item_count):
        result += f'\t{item} \n'
        result += ']'
      else:
        result += f'\t{item}, \n'

    return result
