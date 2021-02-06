# paypal-email-reader
This Python script takes specific information from Paypal's payment confirmation emails and collates them into a csv document

I've recently finished a course on Python programming. I understood most of the concepts but I didn't feel like I was ready to start programming. So I started to take another course. While I was still learning new concepts and rehashing older ones in this new course, I was getting a bit frustrated and bored. I realised I needed a programming project I cared about to delve into. So I scrapped the course I was doing and started to think about something that needed automating! This is where this Paypal idea came from!


I know of someone who receives payments via Paypal and often would get loads of confirmaion emails. So I decided to try to write a script that would take specific information from these emails and collate them into a csv document. The information taken from the emails are: Date, Name of Payer, Invoice Number, Amount Paid and Currency. 


I wanted the script to do everything automatically. However, I realised that 'Title row' of the csv document was continuously inserted every time the script ran. (I need to figure out how to deal with this repetition). So I created a csv file with the title row and the script would now just fill in the relevant data. 

I found this enjoyable and I think it's a useful script! 
