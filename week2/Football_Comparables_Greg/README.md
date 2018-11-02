# Football_Comparables
Basic interface to query historical (since 1992) NFL receiving and rushing data to find historical comparables.

This current iteration of the FBComps module should be able to compare ANY data that meets the folowing requirements:
* All columns must be continuous values (i.e. int or float), categorical values will throw an error.
* The index is currently the reference it spits back upon comparison, so indices should be text or some format that the user might understand (don't use default 0-incremented indices unless they mean something to you)
* Multiple columns that have the index need another unique identifier (if they exist), such as "PlayerName+Season" as opposed to just a name. Otherwise there is a high likelihood of redundant names returned without any differentiation
* Data must be in `.csv` format

The user searches by index values, and they must be typed as they appear in the csv file, as the program searches indices to acquire the starting data that we want to compare to.