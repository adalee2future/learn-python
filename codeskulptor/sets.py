# Examples of Sets

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

inst2 = set(['Rixner', 'Rixner', 'Warren', 'Greiner', 'Wong'])
print inst2

print instructors == inst2

for inst in instructors:
    print inst
    
instructors.add('Cobert')
print instructors
instructors.add('Rixner')
print instructors

instructors.remove('Wong')
print instructors

print 'Rixner' in instructors
print 'Wong' in instructors

def get_rid_of(inst_set, starting_letter):
    remove_set = set([])
    for inst in inst_set:
        if inst[0] == starting_letter:
            remove_set.add(inst)
    inst_set.difference_update(remove_set)
    
get_rid_of(instructors, 'G')
print instructors
