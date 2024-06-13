def read_all_links_from_csv():
    with open('links.csv') as f:
      all_links = []
      lines = f.readlines()
      for line in lines:
          all_links.append(line.split(",")[1].replace("\n", "").strip())
      return all_links