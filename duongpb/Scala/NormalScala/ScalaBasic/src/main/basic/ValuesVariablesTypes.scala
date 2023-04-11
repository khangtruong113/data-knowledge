object ValuesVariablesTypes extends App {
  val x =  42
  //val cannot be reassign, they are IMMUTABLE

  //type of val are optional, it can infer the data type from the input data

  val aString: String = "hello"; val anotherString = "goodbye"
  // the ";" are optional, but not recommend, normally use to seperate setences when they are in the same line

  val aBoolean: Boolean = false
  val aChar: Char = 'a'
  val anint: Int = x
  val aShort: Short = 4325
  val aLong: Long = 2543154354325435431L
  val aFloat: Float = 2.5f
  //without f float will auto be converted as long
  val aDouble: Double = 3.14

  //variables, variables are MUTABLE, use less in functional programming
  var aVariable: Int = 4

  aVariable = 5 //side effects

}
