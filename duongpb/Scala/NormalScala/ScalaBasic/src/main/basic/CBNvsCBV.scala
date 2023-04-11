
object CBNvsCBV extends App {
  def callByValue(x: Long): Unit = {
    println("by value " + x)
    println("by value " + x)
  }

  def callByName(x: => Long): Unit = {
    println("by name " + x)
    println("by name " + x)
  }

  callByValue(System.nanoTime())
  callByName(System.nanoTime())
  // the call by value, the variable and it's value is calculate just when the function create and then it pass to the function
  // call by name, the value is calculate everytime it got call inside the function, it will create when it's being call

}