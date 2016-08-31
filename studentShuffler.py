#======INTRODUCTION=============================================================
# Title:        CST 286 Student Shuffler
#
# Objective:    Print out a seating arrangement for CST 286, in which students
#               are shuffled randomly between CS++ and CSin3 cohorts, with an
#               alternating pattern. I.E: CS++, CSin3, CS++, CSin3, etc.
#
# Objective 2:  To construct the code in a way, such that at the end of CST 286
#               students should be able to understand it themselves.
#
# Author:       Kirk Worley
# Co-Author:    Alyssia Goodwin
#
# Date:         8.27.16
#
# Professor:    Sathya Narayanan
#
# Class:        CST 286 // T.A
#===============================================================================
#======BEGIN PROGRAM============================================================

# Import random library as necessary with alias 'rn'.
#                   It's always necessary. 
import random as rn

#------BEGIN MAIN CODE----------------------------------------------------------

# Function used to determine amount of tabs needed to keep the names in line
# when printing them out. *ARGS = (name of student, position [e.g 1., 2., etc])
def tabs(name, position):
    # Check if the passed name is a string, and the passed position is an int.
    # Otherwise, raise a valueError.
    if((isinstance(name, str)) and (isinstance(position, int))):

        # Arbitrary variable equal to the length of the currently passed name.
        length = len(name)

        # Conditional branches: Return the appropriate number of tabs based on
        # the length of the name.
        # len < 12      ==> 3 tabs
        # 12 < len < 19 ==> 2 tabs
        # len > 19      ==> 1 tab
        # Special Rule 1: If len < 13 AND pos < 10                  ==> 3 tabs.
        # Special Rule 2: If (len > 19 and len < 24) AND pos < 10   ==> 2 tabs.

        # Three Tabs:
        if(length < 12):
            return '\t\t\t'

        # Special Rule 1:
        elif((length < 13) and (position < 10)):
            return '\t\t\t'

        # Special Rule 2:
        elif((length > 19 and length < 21) and (position < 10)):
            return '\t\t'
        
        # One Tab:
        elif(length > 19):
            return '\t'

        # Two Tabs for everything else:
        else:
            return '\t\t'

    # If passed name is not a string, raise a valueError with prompt.
    else:
        raise ValueError("""Passed name must be a string and passed
                         position must be an integer.""")
#------END OF 'tabs()' FUNCTION-------------------------------------------------

# Main function declaration and definition.
def main():

#======EDITABLE PARTS===========================================================
    # Create two arrays of students, one for each cohort.
    # CSPP  =   CS++ Cohort 3
    # CSI3  =   CS in 3 Cohort 4
    # Modularity Check: Able to add students names at will and will still work.
    
    CSPP = [
        'Erick Acedo',
        'Esmeralda Aguayo Vaca',
        'Rosario Araujo',
        'Jaynicka Arrieta',
        'Isaac Avila',
        'Elijah Baird',
        'Santiago Bruno Gonzales',
        'Jonathon Cabrera',
        'Maryann Cortez',
        'Aldrin Carlos',
        'Esteban Flores',   # Check enrollment?
        'Yazmin Hernandez',
        'Julia Jimenez',
        'Andy Kor',
        'Sam Laitha',
        'Martin Landin',
        'Sandra Maciel',
        'Cean Manzano',
        'Priscilla Nunez',
        'Alexis O\'Neill',
        'Carolina Pantoja',
        'Humberto Quintero Cortez',
        'Jeremy Shaw',
        'Niall Shelley',
        'Gavin Todd',
        'Justin Tyler',
        'Antonio Vega',
        'Tiffany Verner',
        'Jordan Wells',
        #'Test Student 1',
        # Extra Students Here
        ]

    CSI3 = [
        'Chino Abatol',
        'Miguel Aceves',
        'Marco Aguilera',
        'Jay Arellano',
        'Jashmae Baculpo',
        'Jose Crescencio',
        'Gilbert Curbelo',
        'Raymond Esteybar',
        'Anakareli Gonzales',
        'Eros Gonzalez-Lopez',
        'Irais Gopar',
        'Emmanuel Guido',
        'Jorge Isaias',
        'Celina Juarez',
        'Raju Kumar',
        'Andrea Lara',
        'Sampson Liao',
        'Brian Martinez Castaneda',
        'Ariel McCarthy',   # Check if correct name?
        'Vanessa Nava',
        'Remberto Nunez',
        'Daniel Ochoa Aguilla',
        'Mayra Ochoa',
        'Reyna Ortiz Ramirez',
        'Oscar Ramirez',
        'Judith Ramirez',
        'Joshua Saavedra',
        'Fernando Sanchez',
        'Faith Shatto',
        'Genesis Valdez',
        'Luis Valencia',
        'Ariana Vargas',
        'Raquel Zempoalteca',
        #'Test Student 2',
        # Extra Students Here
        ]

#======END EDITABLE PARTS=======================================================

    # Using random's shuffle() method, shuffle the two lists.
    rn.shuffle(CSPP)
    rn.shuffle(CSI3)

    # Make one large array to read from. CSI3 > CS++, therefore there
    # will be 2-3 CSI3 students next to each other at the end of the
    # alternating list.
    COMBINED = []

    # Alternate students to the 'COMBINED[]' list starting with CSI3
    # (33 students) and then to CS++ (29 students). Once counter variable
    # passes len(CSPP), append the remaining CSI3 students.
    for i in range(len(CSI3)):
        if(i > (len(CSPP) - 1)):
            COMBINED.append(CSI3[i])
        else:
            COMBINED.append(CSI3[i])
            COMBINED.append(CSPP[i])
            
#------DEBUGGING PURPOSES-------------------------------------------------------
    ### Uncomment to check if the COMBINED[] list has all students.
    ##print COMBINED
    ##print len(COMBINED)
#-------------------------------------------------------------------------------

    # Arbitrary counting variable.
    num = 0

    # Abritary length variable for the following loop, based off of
    # COMBINED / 3 (since we are printing 3 names per line, we only need
    # iterate half as much. But if COMBINED % 2 == 1 then we will miss a
    # student. This is to prevent missing a student.
    #   Length = Factor of 3:        
    if(len(COMBINED) % 3 == 0):
        LENGTH = len(COMBINED) / 3

        #---DEBUGGING PURPOSES---#
        ##print LENGTH

    #   Length != Factor of 3:          
    elif(len(COMBINED) % 3 != 0):
        LENGTH = (len(COMBINED) / 3) + 1

        #---DEBUGGING PURPOSES---#
        ##print LENGTH
    
    # Print the COMBINED list with numbers and 2 names per line.
    # Since there are two names per line, only iterate half the length of
    # COMBINED[].
    for i in range(LENGTH):

        #   Conditional:
        # If __i__ reaches the last iteration, and there is only one name to
        # display (i.e Number of Students is not a factor of 3) then
        # only display a single name, without calling the 'tabs()' function.
        if((len(COMBINED) %3 == 1) and (i == LENGTH-1)):
            print str(num+1) + '. ' + COMBINED[num]         #Single name

        #   Conditional Elif:
        # If __i__ reaches the last iteration, and there is only two names to
        # display (i.e There are an even number of students in COMBINED[]) then
        # only display a two names, calling the 'tabs()' function once.
        elif((len(COMBINED) % 3 == 2) and (i == LENGTH-1)):
            print (str(num+1) + '. ' + COMBINED[num]        # First name
                   + tabs(COMBINED[num], num+1)             # Tabs for space
                   + str(num+2) + '. ' + COMBINED[num+1])   # Second name

        #   Else:
        # There are three names to display. Display the arbitrary counting
        # number (+1 because it starts at 0, and the first student should
        # be '1. X') Call the tabs() function to keep the numbers flush, and
        # then the second student's number and name. Finally, the third
        # student's number and name.
        else:
            print (str(num+1) + '. ' + COMBINED[num]        # First name
                   + tabs(COMBINED[num], num+1)             # Tabs for space
                   + str(num+2) + '. ' + COMBINED[num+1]    # Second name
                   + tabs(COMBINED[num+1], num+2)           # Tabs for space
                   + str(num+3) + '. ' + COMBINED[num+2]    # Third name
                   + '\n')                                  # Line break
        
        # Increase the arbitrary counting variable by 3 for the next
        # three names.
        num += 3

    #=========================================================================#
    # Authors Note:                                                           #
    #-------------------------------------------------------------------------#
    # Because of the alternating pattern, with 2 names per line, CS++ will    #
    # always be on the right side and CSin3 will be on the left side, aside   #
    # from the students at the end of the shuffled CSin3 list.                #
    # Future script should display 3 names per line.                          #  
    #=========================================================================#

#------END MAIN FUNCTION--------------------------------------------------------
#
#                         Modularity Sentinel:
#-------------------------------------------------------------------------------
# If imported, can still be run through the following code:
# import studentShuffler
# studentShuffler.main()
#
#------MODULARITY SENTINEL------------------------------------------------------
if(__name__ == '__main__'):
    main()

#======END OF PROGRAM===========================================================
