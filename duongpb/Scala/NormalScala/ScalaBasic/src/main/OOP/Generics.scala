package main.OOP

object Generics extends App {

  class MyList[A]{
    //use type A in class definition
    def add[B >: A](element: B): MyList[B] = ???
    // if we pass in a parent class of A then the list became list of B

  }
  //another example
  class MyMap[Key, Value]

  val listOfIntegers = new MyList[Int]
  val listOfStrings = new MyList[String]

  //generic methods
  object MyList {
    def empty[A]: MyList[A] = ???

    // take a generic A and then return method A
  }

  val emptyListOfIntegers = MyList.empty[Int]


  //variance problem
  class Animal
  class Cat extends Animal
  class Dog extends Animal

  // 1. List[Cat] extends List[Animal] = COVARIANCE

  class corarianceList[+A]

  val animal: Animal = new Cat
  val animalList: corarianceList[Animal] = new corarianceList[Cat]

  // animalList.add(new Dog) ???

  //2. NO = INVARIANCE in scala
  class InvarianceList[A]
  val invariantAnimalList: InvarianceList[Animal] = new InvarianceList[Animal]

  //3. Hello NO !-> CONTRAVARIANCE

  class ContravariantList[-A]
  val contravariantList: ContravariantList[Cat] = new ContravariantList[Animal]
//  for example
  class Trainer[-A]
  val trainer: Trainer[Cat] = new Trainer[Animal]

  //bounded types
  class Cage[A <: Animal]
  //this list only take the subtype of Animal
}
