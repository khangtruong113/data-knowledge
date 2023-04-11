package main.OOP

object AbstractDataTypes extends App {
  // abstract
  abstract class  Animal {
    val creatureType: String
    def eat: Unit
  }

  class Dog extends Animal {
    override val creatureType: String = "Canine"
    def eat: Unit= println("crunch")
  }

  //traits : like interface
  trait Carnivore {
    def eat(animal: Animal): Unit
  }

  class Crocodile extends Animal with Carnivore{
    val creatureType: String = "croc"

    def eat(animal: Animal): Unit = s"I m a croc and I m eating your ${animal.creatureType}"

    def eat: Unit = "nom nom nom"
  }

  val dog = new Dog
  val croc = new Crocodile
  croc.eat(dog)

  //traits vs abstract claases
  //1 - traits do not have constructor parameters
  //2 - multiple traits may be inherited by the same class
  // 3 - traits - behavior, abstract class = "thing" relationship



}
