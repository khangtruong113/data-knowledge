package main.OOP

object CaseClasses extends App {

  /*
  equals, hashcode, toString
  */
  case class Person(name:String, age:Int)

  //1 - class parameters are fields
  val jim = new Person("Jim", 34)
  println(jim.name)

  //2 - sensible toString, it makes toString print a visuable class instance
//  println(instance) = println(instance.toString())
  println(jim)

  //  3 - equals and hashCode implemented OOTB
  val jim2 = new Person("Jim", 34)
  println(jim == jim2)

  //  4 - ccs have handy copy method
  val jim3 = jim.copy(age = 45)

  //5. case classes have companion object
  val thePerson = Person
  val mary = Person("Mary", 23)

  // 6. Case classes are serializable ( SERIALIZABLE )
  //7. case classes have extractor pattern = case classes can be used in PATTERN MATCHING

  case object UnitedKingdom {
    def name:String = "the UK of CV and NI"
  }
}
