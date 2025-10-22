package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {
  rand.Seed(time.Now().UnixNano())
  isHeistOn := true
  eludedGuards := rand.Intn(100)

  if eludedGuards >= 50 {
    fmt.Println("Looks like you've managed to make it past the guards. Good job, but remember, this is the first step.")
  } else {
    isHeistOn = false
    fmt.Println("Plan a better disguise next time?")
  }
  
  if openedVault := rand.Intn(100); isHeistOn && openedVault >= 70 {
    fmt.Println("Grab and GO!")
  } else if isHeistOn {
    isHeistOn = false
    fmt.Println("Couldn't crack the vault.. Better luck next time!")
  }

  if isHeistOn {
    switch leftSafely := rand.Intn(5); leftSafely {
      case 0:
        isHeistOn = false
        fmt.Println("Caught on camera! Why didn't you wear a mask?")
      case 1:
        isHeistOn = false
        fmt.Println("Vault doors don't open from the inside...")
      case 2:
        isHeistOn = false
        fmt.Println("Bad luck, the police were training a bank heist scenario... bad timing!")
      case 3:
        isHeistOn = false
        fmt.Println("Tripped and fell... oof.")
      default:
        fmt.Println("Start the getaway car!")
    }
  }

  if isHeistOn {
    amtStolen := 10000 + rand.Intn(1000000)
    fmt.Printf("Congrats you got away with: $%v\n", amtStolen)
  }

  fmt.Println(isHeistOn)
}
