from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home Page"""
    return render_template('index.html')

@app.route('/programs')
def programs():
    """Programs Page"""
    programs = [
        {
            'name': 'Soccer',
            'age_group': 'All Ages',
            'description': 'Develop soccer skills, foster creativity, and enhance motor skills through fun-filled games and challenges.',
            'features': ['Skill Development', 'Creative Play', 'Motor Skills Enhancement'],
            'icon': 'fa-soccer-ball'
        },
        {
            'name': 'Art Classes',
            'age_group': '4-18 Years',
            'description': 'Innovative curriculum design in visual arts education blending imaginative thinking with professional techniques.',
            'features': ['Fine Art for Kids (4-12)', 'Fine Art for Teens (11-18)', 'Professional Instruction'],
            'icon': 'fa-palette'
        },
        {
            'name': 'Gymnastics',
            'age_group': 'All Ages',
            'description': 'Vibrant gymnastics program offering diverse classes from beginner to advanced levels.',
            'features': ['Kindergym & KinderStars', 'Aerial Arts (Silks, Trapeze)', 'Structured Progression'],
            'icon': 'fa-child'
        },
        {
            'name': 'Basketball',
            'age_group': '3-18 Years',
            'description': 'Dynamic basketball program designed to develop skills, foster teamwork, and encourage love for the game.',
            'features': ['Tiny Hoopers (3-5)', 'Junior Ballers (6-8)', 'Teen Hoops (13-18)'],
            'icon': 'fa-basketball-ball'
        },
        {
            'name': 'Swimming',
            'age_group': '6 Months - Adult',
            'description': 'Comprehensive swim program prioritizing safety and confidence for swimmers of all ages and skill levels.',
            'features': ['Infant Classes', 'Adult Lessons', 'Professional Instructors'],
            'icon': 'fa-swimmer'
        }
    ]
    return render_template('programs.html', programs=programs)

@app.route('/soccer')
def soccer():
    """Soccer Program Page"""
    soccer_info = {
        'title': 'Soccer Program',
        'description': 'An exciting and enriching after-school activity led by passionate coaches dedicated to nurturing your child\'s love for the game.',
        'features': [
            'Developmentally appropriate techniques for each skill level',
            'Creative play and innovative techniques',
            'Fun-filled games and challenges to improve coordination',
            'Supportive learning environment'
        ],
        'schedule': [
            {'location': 'Barron Park', 'time': 'Mondays, 3:00-4:00 PM'},
            {'location': 'Lucille Nixon', 'time': 'Tuesdays, 2:10-3:40 PM'},
            {'location': 'Ohlone', 'time': 'Wednesdays, 2:00-3:00 PM'},
            {'location': 'Palo Verde', 'time': 'Thursdays, 2:45-3:45 PM'},
            {'location': 'Heritage Park', 'time': 'Saturdays, 3:00-4:00 PM'},
            {'location': 'Heritage Park', 'time': 'Sundays, 11:00-12:00 PM'}
        ],
        'benefits': [
            'Develop Soccer Skills: Coaching emphasizes developmentally appropriate techniques',
            'Foster Creativity: Focus on creative play and innovative techniques',
            'Enhance Motor Skills: Improve coordination, balance, and overall physical fitness'
        ]
    }
    return render_template('soccer.html', soccer_info=soccer_info)

@app.route('/art')
def art():
    """Art Classes Page"""
    art_info = {
        'title': 'Art Classes',
        'description': 'Innovative curriculum design in visual arts education, seamlessly blending imaginative thinking with professional techniques.',
        'location': '908 Harmon Dr, Menlo Park, CA 94025, USA',
        'programs': [
            {
                'name': 'Fine Art for Kids',
                'age_range': '4-12 years',
                'duration': '1 hour per session',
                'description': 'Nurture creativity and self-expression through engaging, age-appropriate activities designed to inspire young artists while developing fundamental skills.'
            },
            {
                'name': 'Fine Art for Teens',
                'age_range': '11-18 years', 
                'duration': '2 hours per session (1-3 times per week)',
                'description': 'Deeper exploration of artistic techniques and concepts. Students refine skills, experiment with new mediums, and develop their unique artistic voice.'
            }
        ],
        'philosophy': 'Our courses foster artistic talent and instill a lifelong appreciation for the visual arts through dedicated and passionate instruction.'
    }
    return render_template('art.html', art_info=art_info)

@app.route('/gymnastics')
def gymnastics():
    """Gymnastics Program Page"""
    gymnastics_info = {
        'title': 'Gymnastics Program',
        'location': 'Arrillaga Family Gymnastics Center',
        'description': 'A vibrant gymnastics program offering diverse classes designed to inspire and engage young gymnasts of all ages.',
        'programs': [
            {
                'category': 'Parent-Child Classes',
                'classes': ['Kindergym', 'KinderStars'],
                'description': 'Caregivers and children participate together, fostering bonding and early development through interactive activities.'
            },
            {
                'category': 'Independent Classes (Ages 3-6)',
                'classes': ['NewStars', 'MiniStars', 'SuperStars'],
                'description': 'Designed to nurture independent participation and skill-building in a supportive environment.'
            },
            {
                'category': 'Structured Progression (Ages 6+)',
                'classes': ['Level A', 'Level B', 'Level C'],
                'description': 'Structured progression allowing for skill advancement and mastery at each stage.'
            }
        ],
        'specialty_programs': [
            'Silks, Trapeze, and Aerial Arts: Explore the thrill of aerial gymnastics',
            'Stretch and Strength Program: Focus on flexibility and physical conditioning',
            'Exploration Through Movement: Encourages creativity and self-expression through diverse movement techniques'
        ]
    }
    return render_template('gymnastics.html', gymnastics_info=gymnastics_info)

@app.route('/basketball')
def basketball():
    """Basketball Program Page"""
    basketball_info = {
        'title': 'Basketball Program',
        'location': 'Fairmeadow Elementary School and Menlo Park Sports Center',
        'description': 'Dynamic basketball program designed to develop skills, foster teamwork, and encourage a love for the game among young players.',
        'programs': [
            {
                'name': 'Tiny Hoopers',
                'age_range': '3-5 years',
                'description': 'Introductory classes focus on basic basketball skills and coordination through playful, engaging activities. Parents or caregivers are encouraged to participate.'
            },
            {
                'name': 'Junior Ballers',
                'age_range': '6-8 years',
                'description': 'Classes emphasize fundamental skills such as dribbling, shooting, and passing, while promoting teamwork and sportsmanship.'
            },
            {
                'name': 'Youth League',
                'age_range': '9-12 years',
                'description': 'More advanced skill development and game strategy, preparing players for competitive play and enhancing basketball fundamentals.'
            },
            {
                'name': 'Teen Hoops',
                'age_range': '13-18 years',
                'description': 'Focus on refining skills, game tactics, and physical conditioning with advanced coaching and league play opportunities.'
            }
        ],
        'benefits': [
            'Skill development appropriate for each age group',
            'Teamwork and sportsmanship emphasis',
            'Professional coaching and instruction',
            'Opportunities for competitive play'
        ]
    }
    return render_template('basketball.html', basketball_info=basketball_info)

@app.route('/swimming')
def swimming():
    """Swimming Program Page"""
    swimming_info = {
        'title': 'Swimming Program',
        'location': 'Cubberley Community Center',
        'description': 'Making every splash a safe and enjoyable experience while helping our community become more confident and skilled swimmers.',
        'age_range': '6 months old to adults of all ages',
        'philosophy': 'We believe it\'s never too early or too late to learn to swim. Our experienced instructors undergo extensive training to provide the best instruction possible.',
        'programs': [
            {
                'category': 'Infant Swimming',
                'age': '6 months and up',
                'description': 'Gentle introduction to water with parent participation'
            },
            {
                'category': 'Child Swimming',
                'age': 'Toddlers to teens',
                'description': 'Progressive skill development from basic water safety to advanced strokes'
            },
            {
                'category': 'Adult Swimming', 
                'age': 'All adult ages',
                'description': 'Learn to swim or refine existing techniques in a supportive environment'
            }
        ],
        'features': [
            'Experienced instructors with extensive training',
            'Programs for every age group and skill level',
            'Diverse teaching perspectives and techniques',
            'Focus on safety, confidence, and skill development',
            'Supportive and engaging environment'
        ]
    }
    return render_template('swimming.html', swimming_info=swimming_info)

@app.route('/summer-camp')
def summer_camp():
    """Summer Camp Page"""
    camp_info = {
        'title': 'RocketBobKids Summer Camp',
        'subtitle': 'Co-ed Day Camp for Grades K-10',
        'description': 'Our camp inspires campers to try new activities, build independence, make friends, and take home memories that will last a lifetime.',
        'schedule': 'Monday - Friday, 8:50 AM to 4:15 PM',
        'price': '$266 per day',
        'activities': [
            'Arts & Crafts', 'Mountain Biking', 'Creation Station',
            'Outdoor Survival', 'Swimming Pool', 'Sports & Games',
            'Archery', 'Music', 'Rock Wall Climbing'
        ],
        'special_features': [
            'Free choice format - campers design their own schedule',
            'Special Wednesday activities (rock climbing, slip n\' slide, spa sessions)',
            'Nutritious lunch and healthy snacks included',
            'Hot meal options with salad bar and multiple stations'
        ]
    }
    return render_template('summer_camp.html', camp_info=camp_info)

@app.route('/about')
def about():
    """About Page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact Page"""
    contact_info = {
        'email': 'RocketBobKids02@gmail.com',
        'phone': '(650) 569-1741'
    }
    return render_template('contact.html', contact_info=contact_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)