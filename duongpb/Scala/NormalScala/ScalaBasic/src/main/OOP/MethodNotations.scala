package main.OOP

object MethodNotations extends App {

  class Person (val name:String, favouriteMovie:String) {
    def likes(movie: String): Boolean = movie == favouriteMovie
    def hangoutWith(person: Person): String = s"${this.name} is haning out with ${person.name}"
    def unary_! : String = s"$name, what the hell ?"
    def isAlive: Boolean = true

    def apply(): String = "hi"
  }

  val mary = new Person("Mary", "Inception")
  println(mary.likes("Inception"))
  println(mary likes "Inception")
  //this call infix notation = operator notation (syntactic notation)

  //this is the same, but the cool thing is this works if the function have only 1 parameter

  val tom = new Person("Tome", "Fight Club")
  println(mary hangoutWith tom)
  // we can also name function as + or -, .....

  // ALL OPERATOR ARE METHOD NAMABLE

  //prefix notation
  val x = -1 //equivilant with 1.unary_-
  //the same to
  val y = 1.unary_-
  //this unary prefix only works with - + !
  println(!mary)
  //the same to
  println(mary.unary_!)

  //postfix notation, only use for function that is not having any parameter
  println(mary.isAlive)
//  println(mary isAlive)

//apply method
  println(mary.apply())
  println(mary())
  //3when the object is called like a function because the compiler will seek for apply method
}
