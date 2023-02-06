//dois codigos para entender as goroutines (deixei um link na bibliografia do documento tambem)
/*
//codigo mais basico
package main

import (  
    "fmt"
    "time"
)

func hello() {  
    fmt.Println("Hello world goroutine")
}
func main() { //main e uma goroutine implicita
    go hello() //uma goroutine so executa quando outras nao o estao
    time.Sleep(1 * time.Second) //este timer da um tempo nesta goroutine e outras executam neste periodo
    fmt.Println("main function")
}
*/

//codigo um pouco mais complexo
package main

import (  
    "fmt"
    "time"
)

func numbers() {  
    for i := 1; i <= 5; i++ {
        time.Sleep(250 * time.Millisecond)
        fmt.Printf("%d ", i)
    }
}
func alphabets() {  
    for i := 'a'; i <= 'e'; i++ {
        time.Sleep(400 * time.Millisecond)
        fmt.Printf("%c ", i)
    }
}
func main() {  
    go numbers()
    go alphabets()
    time.Sleep(3000 * time.Millisecond)
    fmt.Println("main terminated")
}