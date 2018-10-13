# for each intent you want to create, make a separate file with a class definition
# inherit from Intent. Docs should be clear enough; the metaclass/subclass handler will take care of definition validation.
#
# example
# class DirtyJokesTeller(Intent):
#     INTENT_NAME = 'jokes-teller.dirty'
#     PARAMS = ['topic']  # all params are given as strings
#
#     def handle(topic):
#         if topic == 'any':
#             return "As I suspected, someone has been adding soil to my garden. The plot thickens."
#         else:
#             return "I don't know any jokes on this specific topic :|"
#
