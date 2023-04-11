package main.OOP

object AnomyousClass extends App {
  abstract class Animal {
    def eat: Unit
  }

  val funnyAnimal: Animal = new Animal {
    override def eat: Unit = print("AHAHAHAHAHAHAHAH")
  }

  /**
   * equivalent to
   *class AnonymousClasses$$anon$1 extends Animal {
   *  override def eat: unit = println("AAHAHAHA")
   *
   * }
   * val funnyAnimal: Animal = new AnonymousClasses$$anon$1
   */
  class Person(name:String){
    def sayHi: Unit = println(s"Hi, my name is {$name}, how can I be of service")
  }

  val jim = new Person("Jim"){
    override def sayHi: Unit = println("Hi my name is Jim")
  }

}
