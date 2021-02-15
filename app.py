import os
from flask import Flask, jsonify
app = Flask(__name__)

##be lazy and use tuples for now
##todo: shift this to a sqlite db so I can accept POST requests

bio = [
	{
		'preferred name': 'Nick Barraclough',
		'pronouns': 'he/him',
		'full_name': 'Nicholas Peter Barraclough-Scott',
		'email': 'nick@barraclough.nz',
		'phone': '+44 7496 494933',
		'linkedin' :'https://www.linkedin.com/in/nickbarraclough',
		'education' : 'B.Com. majoring in Accounting & Information Systems, University of Auckland',
		'about':'Dynamic SaaS success manager with a technical slant, supporting worldwide customers with a consultative approach. Have lead implementation for large and complex accounts while providing a high quality of service, following through to success. Confident with technical documentation, and scoping the use cases for API’s to create integrative solutions for end users. Experienced with start-ups and independent work in order to grow products in emerging markets, and collaborative across teams with a variety of technical knowledge.'
	}
]

outside = [
	{
		'description': 'These are some of the things that I do outside of work',
		'volunteering': 'NHS volunteer for the Excel vaccination centre.',
		'hiking': 'Great at getting lost in the outdoors.',
		'kareoke': 'Unskilled singer, make up for this with too much enthusiasm.',
		'humour': 'Make plenty of puns and dad jokes.',
		'coding': 'Okay at SQL, learning Python.'
		}
]

reference = [
	{
		'references': 'Available on request.'
	}
]

experience1 = [
	{
		'id':'1',
		'company': 'Figured',
		'website': 'https://figured.com/',
		'role': 'Partner Success Manager UK & Ireland',
		'product': 'Fintech for agri, building financial management tools to answer the now/where/how on farm to drive profitability.',
		'data': 'Integrating financial (Xero) and production (BCMS, ICBF, AgriWebb, MyJohnDeere) operations for over 30,000 farms worldwide.',
		'summary': ''''- Large scale pilots and implementations of Figured across accountants and banks in an emerging market.
- Consultative approach to involving stakeholders, from top to bottom of a client’s business.
- Building product usage dashboards in Kibana for proactive engagement with clients and quarterly reviews.
- Scoping and assisting development of integrations with government APIs.
- Collaborating closely with international sales, product and service teams for smooth handovers of projects.
- Building sales enablement, training content and running one-to-many sessions in person and online.'''''
	},
{
		'id':'2',
		'company': 'Figured',
		'role': 'Customer Success Manager NZ',
		'summary': ''''- Implemented & supported Figured in a late majority market.
- Launched regular webinars and training sessions to become the voice of Figured.
- Collaborating with product and development teams to scope and test new features.
- Created a support process for triaging and escalating JIRA tickets to work directly with developers.
- Operated client support through in-app chat & direct account support.'''
	},
		{
		'id':'3',
		'company': 'Preno',
		'website': 'https://prenohq.com/',
		'role': 'Head of Sales & Support',
		'product': 'Early stage SaaS start-up, building hotel property management tools.',
		'data': 'Integrating financial data, hotel bookings, and food & beverage together in a single place for hoteliers to run their business.',
		'summary': '''- Wrote & recorded product support documentation, using a combination of text, GIFs, and videos.
- Full cycle sales development, implementation and post-sale customer success.
- Consistent MRR growth per quarter through new sales, increased annual subscriptions.
- Reduced and maintained response times to enable 24/7 support for worldwide customers.
- Designed management reports through HubSpot and Klipfolio to track metrics like churn, conversion, and growth.
'''''
	}
]

#now define the routes/endpoints
#this is just referring to the defined tuples up above, so can only support GET at the moment

@app.route('/')
def welcome():
    # return a blob
    return jsonify({'welome': 'There are three endpoints available: ~/all, ~/bio, ~/experience, ~/outside'})


@app.route('/bio/')
def personalinfo():
    # return a blob
    return jsonify({'bio': bio}
    	)


@app.route('/experience/')
def company():
    # return a blob
    return jsonify({'experience': experience1}
    	)
    

@app.route('/outside/')
def outside():
    # return a blob
    return jsonify({'outside': outside}
    	)

@app.route('/all')
def all():
    # return a blob
    return jsonify(
    	{'bio': bio}, 
    	{'experience': experience1},
    	##why does this suddenly break after you enter a third one?
    	{'outside': outside},
    	{'references': references}
    )



if __name__ == '__main__':
    #defining localhost and the port to use - not sure if this needs to be changed?
    app.run(host='0.0.0.0', port=80)