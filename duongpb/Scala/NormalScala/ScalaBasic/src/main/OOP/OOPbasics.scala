package main.OOP

object OOPbasics extends App {
  val person = new Person("John", 26)

  person.greet("duong")
}

class Person(name: String, val age: Int){
  //body of the class

  def greet(name: String): Unit = {
    println(s" ${this.name} says: Hi, $name")
  }
}

// class parameters are not fields