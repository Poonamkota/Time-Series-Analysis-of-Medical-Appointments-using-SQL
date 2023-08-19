# Module 3 MySQL queries to extract information from patients table

##Task 1: How many values are there in the given dataset
SELECT COUNT(*) FROM patients;


##Task 2: Count the number of appointments for each day in the given dataset
SELECT count(patients.AppointmentDay) as number_of_appointments, patients.AppointmentDay from patients 
group by patients.AppointmentDay


##Task 3: Calculate the average number of appointments(Set to nearest whole number) per day in the given dataset.
select ROUND(AVG(appts)) as avg_appt from 
(select count(*) as appts from patients group by patients.AppointmentDay) sub


##Task 4: Find the day with the highest number of appointments in the given dataset.
select AppointmentDay,count(*) as num_appointments from patients 
group by AppointmentDay 
order by num_appointments desc limit 1


##Task 5: Calculate the monthly average number of appointments in the given dataset.
Select DATE_FORMAT(AppointmentDay, '%Y-%m') as Month, count(*) as num_appointments from patients 
group by Month 
order by num_appointments Asc


##Task 6: Find the month with the highest number of appointments in the given dataset.
select DATE_FORMAT(AppointmentDay, '%Y-%m') as Month, count(*) as num_appointments from patients 
group by Month 
order by num_appointments DESC limit 1


#Task 7: Calculate the weekly average number of appointments in the given dataset
SELECT YEAR(AppointmentDay) AS Year, WEEK(AppointmentDay) AS Week, COUNT(*) AS num_appointments
FROM patients
GROUP BY Year, Week
ORDER BY Year ASC, Week ASC


##Task 8:  Find the week with the highest number of appointments in the given dataset.
SELECT YEAR(AppointmentDay) AS Year, WEEK(AppointmentDay) AS Week, COUNT(*) AS num_appointments
FROM patients
GROUP BY Year, Week
ORDER BY num_appointments DESC LIMIT 1


##Task 9: What is the distribution of appointments based on gender in the dataset?
SELECT Gender,count(Gender) FROM patients GROUP BY gender


##Task 10: Calculate the number of appointments per weekday in the given dataset. Order the appointment counts in descending.
SELECT DAYNAME(AppointmentDay) AS Weekday, COUNT(*) AS num_appointments FROM patients 
GROUP BY Weekday 
ORDER BY num_appointments DESC


##Task 11: Calculate the average time between scheduling and the appointment day in the given dataset. Set to nearest whole number
SELECT ROUND(AVG(DATEDIFF(AppointmentDay, ScheduledDay))) AS avg_time_to_appointment FROM patients
