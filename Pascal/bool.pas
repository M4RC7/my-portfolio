program exBoolean;
var
exit: boolean;

choice: char;
   begin
   writeln('Do you want to continue? ');
   writeln('Enter Y/y for yes, and N/n for no');
   readln(choice);
   (*readln(exit);*){attempting this will result in error}

if(choice = 'n') then
   exit := true
else
   exit := false;

if (exit) then
   writeln(' Good Bye!')
else
   writeln('Please Continue');

(*writeln(exit);*)
{Booleans can be written to output, but not read from input}

readln;
end.
