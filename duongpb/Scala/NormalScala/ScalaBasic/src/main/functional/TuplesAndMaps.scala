package main.functional

object TuplesAndMaps extends App {
  //tuples = finite ordered "lists"
  val aTuple = (2, "hello, scala") // tuple2[Int, String] = (Int, String)

  //we can access tuple elements
  print(aTuple._1) //2
  print(aTuple.copy(_2 = "Goodbye Java"))
  print(aTuple.swap) // ("Hello, Scala", 2)

  // Maps - keys -> Values
  val aMap: Map[String, Int] = Map()
  //map is immutable

  //like a containing list of tuple
  val  phoneBook = Map(("Jim", 555),"Daniel" -> 999).withDefaultValue(-1)
  // with default value is setting in case we call a wrong ket, we will have the return as -1
  // a-> b is sugar for (a,b)

  println(phoneBook.contains("Jim"))
  println(phoneBook("Jim"))

  //add a paring
  val newParing = "Mary" -> 678
  val newPhoneBook = phoneBook + newParing

  //map ops

  //function on map
  //map, filter, flatmap
  println(phoneBook.map(pair => pair._1.toLowerCase -> pair._2))

  //filter keys
  println(phoneBook.filterKeys(x => x.startsWith("J")))

  //mapvalues
  print(phoneBook.mapValues(number => number + 10))

  //conversions to other collection
  print(phoneBook.toList)
  print(List(("Daniel", 555),("James", 432)).toMap)

  val names = List("Bob", "Angela", "mary")
  println(names.groupBy(names => names.charAt(0)))

}
