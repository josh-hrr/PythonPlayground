def get_totals_list(data):
  return [value['total'] for value in data]

def get_sum_totals(totals_list):
  return sum(totals_list)
