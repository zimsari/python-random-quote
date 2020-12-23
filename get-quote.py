import random

last = 13
rnd = random.randint(0, last)

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()


  print(quotes[rnd], end=' ')
  print(quotes[rnd], end=' ')
  print(quotes[rnd], end=' ')

if __name__== "__main__":
  main()
