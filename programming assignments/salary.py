# Alisha Agrawal (aa3se)
"""
retrieve information on a person's job, salary,
and rank from a freely available website.
"""
import urllib.request
import re

f = ""


def report(name):
    """
    takes in a name and returns the
    job, salary, and rank of that person
    """
    global f
    # check if url is valid:
    try:
        name_to_url(change_name(name))
    except:
        job = None
        sal = 0
        ra = 0
        return job, sal, ra
    url = name_to_url(change_name(name))
    f = url.read().decode('utf-8')
    job = job_title()
    sal = salary()
    ra = rank()
    return job, sal, ra


def change_name(name):
    """
    returns a changed name so that
    it can be excepted as a url
    """
    list_name = name.lower().split()
    for part in list_name:
        # remove period:
        if "." in part:
            part = part[:-1]
            list_name[1] = part
            name = '-'.join(list_name)
        # remove and reorder comma
        if "," in part:
            new_part = part[:-1]
            list_name.remove(part)
            list_name.append(new_part)
            name = '-'.join(list_name)
    # only spaces:
    if " " in name:
        name = '-'.join(list_name)
    return name


def name_to_url(name):
    """
    adds a changed/acceptable name to
    a url for future searches
    """
    url_name = change_name(name)
    new_url = urllib.request.urlopen('https://cs1110.cs.virginia.edu/files/uva2018/' + url_name)
    return new_url


def job_title():
    """
    searches and returns the job
    title of a person from their url
    """
    search_job = r'(Job title: ((\w+,?\s?(&#39;|&amp;)?/?\w?\s?)+))|' \
                 r'("personjob">((\w+,?\s?(&#39;|&amp;)?/?\w?\s?)+))'
    search_job_finder = re.compile(search_job)
    matches = search_job_finder.finditer(f)
    for each in matches:
        # case one: "job title:"
        if each.group(2) is not None:
            job = each.group(2)
            if "&amp;" in job:
                index = job.find("&amp;")
                job = job[:index] + "&" + job[index + 5:]
                return job
            if "&#39" in job:
                index = job.find("&#39;")
                job = job[:index] + "'" + job[index + 5:]
                return job
            else:
                return job
        # case two: "personjob"
        if each.group(7) is not None:
            job = each.group(7)
            if "&amp;" in job:
                index = job.find("&amp;")
                job = job[:index] + "&" + job[index + 5:]
                return job
            if "&#39" in job:
                index = job.find("&#39;")
                job = job[:index] + "'" + job[index + 5:]
                return job


def salary():
    """
    searches and returns the salary
    of a person from their url
    """
    search_sal = r'(total gross pay: \$(\d+,?(\d+)?))|' \
                 r'("paytotal">\$(\d+,?(\d+)?))|' \
                 r'(paytype.amount, (\d+,?(\d+)?))'
    search_sal_finder = re.compile(search_sal)
    matches = search_sal_finder.finditer(f)
    for wage in matches:
        # case one: "total gross pay"
        if wage.group(2) is not None:
            sal = wage.group(2)
            comma_index = sal.find(",")
            sal = float(sal[:comma_index] + sal[comma_index + 1:])
            return sal
        # case two: "paytotal"
        if wage.group(5) is not None:
            sal = wage.group(5)
            comma_index = sal.find(",")
            sal = float(sal[:comma_index] + sal[comma_index + 1:])
            return sal
        # case three: "paytype.amount"
        if wage.group(8) is not None:
            sal = wage.group(8)
            comma_index = sal.find(",")
            sal = float(sal[:comma_index] + sal[comma_index + 1:])
            return sal


def rank():
    """
    searches and returns the rank
    of a person from their url
    """
    null_rank = 0
    search_rank = r"rank</td><td>(\d(,)?(\d+)?)"
    search_rank_finder = re.compile(search_rank)
    matches = search_rank_finder.finditer(f)
    for r in matches:
        if r.group(1) is not None:
            if "," in r.group(1):
                c_rank = r.group(1)
                i = c_rank.find(",")
                c_rank = int(c_rank[:i] + c_rank[i + 1:])
                return c_rank
            return int(r.group(1))
        else:
            return null_rank
    return null_rank
