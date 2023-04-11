object StringOps extends App {
  val str: String = "Hello there"

  //indexing
  println(str.charAt(2))
  val newString: String = str.substring(7, 11)
  println(str.split(" ").toList)
  println(str.startsWith("Hello"))
  println(str.replace(" ", "-"))
  println(str.toLowerCase())
  println(str.length)

  val anumberString = "2"
  val aNumnber = anumberString.toInt

  println('a' +: anumberString :+ 'z')
  println(str.reverse)

//  put val into string
  val name = "David"
  val age = 12
  val greeting = s"Hello my name is $name and I am $age years old"

  // Format string
  val speed = 1.2f
  val myth = f"$name can eat $speed%2.2f burgers per minute"

  //raw string
  println(raw"this is a \n new line")
}
