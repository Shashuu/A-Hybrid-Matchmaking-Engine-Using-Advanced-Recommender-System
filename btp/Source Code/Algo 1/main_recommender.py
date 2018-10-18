from collections import defaultdict
import weakref
import operator

# does not care option in any attribute should be set as 999
"""age_distances= [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
height_distances= [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
edu_distances=  [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
income_distances= [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
body_distances= [0.25, 0.25, 0.25, 0.25]
complexion_distances= [0.25, 0.25, 0.25, 0.25]
"""

def apply_property(cls):
		def make_getter(name):
				def getter(self):
						return getattr(self, name)
				return getter

		def make_setter(name):
				def setter(self, val):
						setattr(self, name, val)
				return setter

		for f in cls.fields:
				getter = make_getter('_' + f)
				setter = make_setter('_' + f)
				setattr(cls, f, property(getter, setter))
		return cls


class KeepRefs(object):
		__refs__ = defaultdict(list)

		def __init__(self):
				self.__refs__[self.__class__].append(weakref.ref(self))

		@classmethod
		def get_instances(cls):
				for inst_ref in cls.__refs__[cls]:
						inst = inst_ref()
						if inst is not None:
								yield inst


@apply_property
class User(KeepRefs):
		"""docstring for User"""
#    user_instances = []
		fields=['uid','age','height','religion','caste', 'education', 'occupation','income', 'body','complexion','diet','smoke','drink','recommendations','age1','height1','religion1','caste1', 'education1', 'occupation1','income1', 'body1','complexion1','diet1','smoke1','drink1']

		def __init__(self, uid, age, height, religion, caste, education, occupation, income, body, complexion, diet, smoke, drink, age1, height1, religion1, caste1, education1, occupation1, income1, body1, complexion1, diet1, smoke1, drink1, weights, age_counts = None, height_counts = None, edu_counts = None, income_counts = None, body_counts = None, complexion_counts = None):
				super(User, self).__init__()
#profile
				self.uid = uid
				self.age = age
				self.height = height
				self.religion = religion
				self.caste = caste
				self.education = education
				self.occupation = occupation
				self.income = income
				self.body = body
				self.complexion = complexion
				self.diet = diet
				self.smoke = smoke
				self.drink = drink
#preferences
				self.age1 = age1
				self.height1 = height1
				self.religion1 = religion1
				self.caste1= caste1
				self.education1 = education1
				self.occupation1 = occupation1
				self.income1 = income1
				self.body1 = body1
				self.complexion1 = complexion1
				self.diet1 = diet1
				self.smoke1 = smoke1
				self.drink1 = drink1

				self.weights = weights
				self.recommendation_objects = []
				self.recommendations_scores = {}

				self.age_counts = age_counts if age_counts is not None else None
				self.height_counts = height_counts if height_counts is not None else None
				self.edu_counts = edu_counts if edu_counts is not None else None
				self.income_counts = income_counts if income_counts is not None else None
				self.body_counts = body_counts if body_counts is not None else None
				self.complexion_counts = complexion_counts if complexion_counts is not None else None

				self.type = 0 if self.age_counts is None else 1
#        self.__class__.instances.append(weakref.proxy(self))
		
		def get_recommendations(self):
			return sorted(self.recommendations_scores.items(), key=operator.itemgetter(1), reverse=True)

class CrispCheck(object):
		def __init__(self, u1, u2):
			super(CrispCheck, self).__init__()
			#self.res = 0
			if(CrispCheck.ultimate_check(u1, u2)):
				getattr(u1, 'recommendation_objects').append(u2)
				#if u1.type == 0:
				Scorer(u1, u2, u2.uid)
				#else:
					#Scorer_adv(u1, u2, u2.uid)


				



		@staticmethod
		def religion_check(u1, u2):
			if (u1.religion1 == u2.religion) or u1.religion1 == 999:
				return 1

		@staticmethod
		def caste_check(u1, u2):
			if (u1.caste1 == u2.caste) or u1.caste1 == 999:
				return 1

		@staticmethod
		def occupation_check(u1, u2):
			if (u1.occupation1 == u2.occupation) or u1.occupation1 == 999:
				return 1
		@staticmethod
		def diet_check(u1, u2):
			if (u1.diet1 == u2.diet) or u1.diet1 == 999:
				return 1

		@staticmethod
		def smoke_check(u1, u2):
			if (u1.smoke1 == u2.smoke) or u1.smoke1 == 999:
				return 1

		@staticmethod
		def drink_check(u1, u2):
			if (u1.drink1 == u2.drink) or u1.drink1 == 999:
				return 1

		@classmethod
		def ultimate_check(cls, u1, u2):
			func_list=[cls.religion_check, cls.caste_check, cls.occupation_check,
					cls. diet_check, cls.smoke_check, cls.drink_check]
			return all(func(u1, u2) for func in func_list)

			# if cls.religion_check(u1, u2) and cls.caste_check(u1, u2) and cls.occupation_check(u1, u2) and cls.diet_check(u1, u2) and cls.smoke_check(u1, u2) and cls.drink_check(u1, u2)


class Scorer(object):
		"""docstring for Scorer"""
		#def __init__(self, weights, age_dist, height_dist, edu_dist, income_dist, body_dist, compl_dist):
		age_distances= [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
		height_distances= [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
		edu_distances=  [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
		income_distances= [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
		body_distances= [0.25, 0.25, 0.25, 0.25]
		complexion_distances= [0.25, 0.25, 0.25, 0.25]
		def __init__(self, u1, u2, userid):
			super(Scorer, self).__init__()
			self.userid= userid
			self.score = Scorer.calculator(u1, u2) if u1.type == 0 else Scorer.calculator_adv(u1, u2)
			getattr(u1, 'recommendations_scores').update({self.userid:self.score})

			
		
		@classmethod
		def age_score(cls, u1, u2):
			t1=u1.age1
			t2=u2.age
			t1, t2 = sorted([int(t1),int(t2)])
			age_dist=0
			for value in cls.age_distances[int(t1):int(t2)]:
				age_dist = age_dist + value

			return u1.weights[0] * (1 - age_dist)

		@classmethod
		def height_score(cls, u1, u2):
			t1 = u1.height1
			t2 = u2.height
			t1, t2 = sorted([int(t1),int(t2)])
			height_dist=0
			for value in cls.height_distances[int(t1):int(t2)]:
				height_dist  = height_dist + value

			return u1.weights[1] * (1 - height_dist)

		@classmethod
		def edu_score(cls, u1, u2):
			t1 = u1.education1
			t2 = u2.education
			t1, t2 = sorted([int(t1),int(t2)])
			edu_dist=0
			for value in cls.edu_distances[t1:t2]:
				edu_dist  = edu_dist + value

			return u1.weights[2] * (1 - edu_dist)

		@classmethod
		def income_score(cls, u1, u2):
			t1 = u1.income1
			t2 = u2.income
			t1, t2 = sorted([int(t1),int(t2)])
			inc_dist=0
			for value in cls.income_distances[int(t1):int(t2)]:
				inc_dist = inc_dist + value

			return u1.weights[3] * (1 - inc_dist)

		@classmethod
		def body_score(cls, u1, u2):
			t1 = u1.body1
			t2 = u2.body
			t1, t2 = sorted([int(t1),int(t2)])
			body_dist=0
			for value in cls.body_distances[int(t1):int(t2)]:
				body_dist = body_dist + value

			return u1.weights[4] * (1 - body_dist)

		@classmethod
		def complexion_score(cls, u1, u2):
			t1 = u1.complexion1
			t2 = u2.complexion
			t1, t2 = sorted([int(t1),int(t2)])
			compl_dist=0
			for value in cls.complexion_distances[int(t1):int(t2)]:
				compl_dist = compl_dist + value

			return u1.weights[5] * (1 - compl_dist)


		@classmethod
		def calculator(cls, u1, u2):
			return cls.age_score(u1, u2) + cls.height_score(u1, u2) + cls.edu_score(u1, u2) + cls.income_score(u1, u2) + cls.body_score(u1, u2) + cls.complexion_score(u1, u2)


		@classmethod
		def age_score_adv(cls, u1, u2):
			t1=u1.age1
			t2=u2.age
			counts = u1.age_counts
			counts = [float(i)/counts[t1-1] for i in counts]
			#print('counts is')
			#print(counts)
			#print('age wt is')
			#print((counts[t2-1] if counts[t2-1]<1 else 0.98))
			return u1.weights[0] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def height_score_adv(cls, u1, u2):
			t1 = u1.height1
			t2 = u2.height
			counts = u1.height_counts
			counts = [float(i)/counts[t1-1] for i in counts]
			return u1.weights[1] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def edu_score_adv(cls, u1, u2):
			t1 = u1.education1
			t2 = u2.education
			counts = u1.edu_counts
			counts = [float(i)/counts[t1-1] for i in counts]
			return u1.weights[2] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def income_score_adv(cls, u1, u2):
			t1 = u1.income1
			t2 = u2.income
			counts = u1.income_counts
			counts = [float(i)/counts[t1-1] for i in counts]
			return u1.weights[3] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def body_score_adv(cls, u1, u2):
			t1 = u1.body1
			t2 = u2.body
			counts = u1.body_counts
			counts = [float(i)/counts[t1-1] for i in counts]
			return u1.weights[4] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def complexion_score_adv(cls, u1, u2):
			t1 = u1.complexion1
			t2 = u2.complexion
			counts = u1.complexion_counts
			counts = [float(i)/counts[t1-1] for i in counts]
			return u1.weights[5] * (counts[t2-1] if counts[t2-1]<1 else 0.98)



		@classmethod
		def calculator_adv(cls, u1, u2):
			return cls.age_score_adv(u1, u2) + cls.height_score_adv(u1, u2) + cls.edu_score_adv(u1, u2) + cls.income_score_adv(u1, u2) + cls.body_score_adv(u1, u2) + cls.complexion_score_adv(u1, u2)


"""
class Scorer_adv(object):
		def __init__(self, u1, u2, userid):
			super(Scorer_adv, self).__init__()
			self.userid= userid
			self.score = Scorer_adv.calculator(u1, u2)
			getattr(u1, 'recommendations_scores').update({self.userid:self.score})

			
		
		@classmethod
		def age_score(cls, u1, u2):
			t1=u1.age1
			t2=u2.age
			counts = u1.age_counts
			counts = [i/counts[t1-1] for i in counts]
			return u1.weights[0] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def height_score(cls, u1, u2):
			t1 = u1.height1
			t2 = u2.height
			counts = u1.height_counts
			counts = [i/counts[t1-1] for i in counts]
			return u1.weights[1] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def edu_score(cls, u1, u2):
			t1 = u1.education1
			t2 = u2.education
			counts = u1.edu_counts
			counts = [i/counts[t1-1] for i in counts]
			return u1.weights[2] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def income_score(cls, u1, u2):
			t1 = u1.income1
			t2 = u2.income
			counts = u1.income_counts
			counts = [i/counts[t1-1] for i in counts]
			return u1.weights[3] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def body_score(cls, u1, u2):
			t1 = u1.body1
			t2 = u2.body
			counts = u1.body_counts
			counts = [i/counts[t1-1] for i in counts]
			return u1.weights[4] * (counts[t2-1] if counts[t2-1]<1 else 0.98)

		@classmethod
		def complexion_score(cls, u1, u2):
			t1 = u1.complexion1
			t2 = u2.complexion
			counts = u1.complexion_counts
			counts = [i/counts[t1-1] for i in counts]
			return u1.weights[5] * (counts[t2-1] if counts[t2-1]<1 else 0.98)



		@classmethod
		def calculator(cls, u1, u2):
			return cls.age_score(u1, u2) + cls.height_score(u1, u2) + cls.edu_score(u1, u2) + cls.income_score(u1, u2) + cls.body_score(u1, u2) + cls.complexion_score(u1, u2)

"""
#a = User(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,[1,2,3,4,5,6], )
#b = User(2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,[1,2,3,4,5,6])
#CrispCheck(a,b)
#print(a.recommendation_objects)
#print(a.recommendations_scores)
"""male1 =  User(11, 1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,1,3,2,5,2,2,1,1,1,[10,10,10,10,10,10])
female1 = User(21, 4,6,1,1,5,2,3,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female2 = User(22, 3,5,1,1,6,2,4,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female3 = User(23, 6,3,1,1,6,2,8,3,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female4 = User(24, 2,2,1,1,2,2,5,3,3,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female5 = User(25, 4,4,1,1,4,2,2,4,4,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
#female6 = 
#female7 = 
#female8 = 

CrispCheck(male1, female1)
CrispCheck(male1, female2)
CrispCheck(male1, female3)
CrispCheck(male1, female4)
CrispCheck(male1, female5)
print(male1.get_recommendations())
"""

"""male1 = User(11, 1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,1,3,1,5,2,2,1,1,1,[10,10,10,10,10,10], [10,10,10,30,10,10,20,40], [10,10,10,30,10,10,10,50], [10,10,30,30,20,50], [10,10,10,30,10,10,10,50], [20,30,40,50], [20,40,30,50])
female1 = User(21, 3,3,1,1,2,1,4,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female2 = User(22, 8,8,1,1,6,1,10,4,4,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
CrispCheck(male1, female1)
CrispCheck(male1, female2)
print(male1.get_recommendations())
"""

male1 =  User(11, 1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,1,3,2,5,2,2,1,1,1,[10,10,10,10,10,10], [10,10,20,30,20,10,20,20], [10,10,10,30,30,10,10,30], [10,20,50,30,20,10], [10,10,10,30,10,10,30,30], [20,20,40,60], [20,40,50,30])
female1 = User(21, 4,6,1,1,5,2,3,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female2 = User(22, 3,5,1,1,6,2,4,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female3 = User(23, 6,3,1,1,6,2,8,3,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female4 = User(24, 2,2,1,1,2,2,5,3,3,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
female5 = User(25, 4,4,1,1,4,2,2,4,4,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2, [10,10,10,10,10,10])
#female6 = 
#female7 = 
#female8 = 

CrispCheck(male1, female1)
CrispCheck(male1, female2)
CrispCheck(male1, female3)
CrispCheck(male1, female4)
CrispCheck(male1, female5)
print(male1.get_recommendations())