// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
int[] data = Enumerable. Range (1, 20) . Select (e = new Random () . Next (10)) . ToArray ();
Console.WriteLine ($"{String.Join(' ', data)}");
// var res = data.GroupBy (e = e);
foreach (var item in res) Console.WriteLine($" {item. Key} {item. Count()} ");
