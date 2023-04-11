package main.OOP

object InheritanceAndTraits extends App {
  class Animal {
    val creatureType = "wild"
    def eat = println("nom nom")
    //set this function to private then it's only visuable in this class, same to protected and public
  }

  class Cat extends Animal{
    def crunch = {
      eat
      println("crunch crunch")
    }
  }

  val cat = new Cat
  cat.eat

  // constructor
  class Person(name: String, age: Int){
    def this(name: String) = this(name, 0)
    // another constructor
  }
  class Adult(name: String, age: Int, idCard: String) extends Person(name)
  //jvm will call the constructor for the parent class first, we can call this constructor as well since we declare it above

  //we can even override in the parameter when we declare a class
  class Dog(override val creatureType: String) extends Animal{
//    override val creatureType = "dosmetic"
    //SUPER : use if you want to refer something from parent class
  override def eat={
      super.eat
      println("crunch, crunch")
    }

  }

  // we can override parents method, values and val as well.
  //  val dog = new Dog
  //  dog.eat
  val dog2 = new Dog("K9") //directly overriding the class Dog with new creature type
  println(dog2.creatureType)

  //POLYMORPHISM

  val unknownAnimal: Animal = new Dog ("K9")
  unknownAnimal.eat

  //OVERLOADING

  //prevent OVERRIDING
// 1 - use final + def/val -> use final on member, final can be use for the class itself
// 2 - use final on the entire class
// 3 - sealed the class, the class can be extended in this file, not from another files

}
