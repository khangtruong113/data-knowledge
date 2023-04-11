package main.OOP

class Objects extends App {
  //SCALA does NOT HAVE CLASS_LEVEL FUNCTIONALITY ("static")
  object Person{ //declare type _ it's only instance
    //'static'/'class' - level functionality
    val N_EYES = 2
    def canFly: Boolean = false

    // factory method: because it used to build another object person
    def from(mother:Person, father: Person): Person = new Person("Bobbie")

//    if this part we use apply()
    def apply(mother:Person, father: Person): Person = new Person("bob")
  }

  class Person(val name: String){
    //instance-level functionality

  }
  //Scala companion happens when both scala object and class with the same name happen and it can access one another

  println(Person.N_EYES)
  println(Person.canFly)
  //SCALA object = Singleton INSTANCE
  val mary = new Person("mary")
  val john = new Person("John")

  println(mary == john)
//  if 2 instance of 2 class -> comparison would be false
  val bob = Person(mary, john)

  // Scala Applications = Scala Object with :
  // def main(args: Array[String]): Unit


}
