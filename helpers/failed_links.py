import pandas as pd


def write_to_failed_links_csv(links, filename):
  df = pd.DataFrame({"failed_links":links})
  df.to_csv(f"{filename}.csv")