
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_CORBA_DynAn_gnuDynStruct__
#define __gnu_CORBA_DynAn_gnuDynStruct__

#pragma interface

#include <gnu/CORBA/DynAn/RecordAny.h>
#include <gcj/array.h>

extern "Java"
{
  namespace gnu
  {
    namespace CORBA
    {
      namespace DynAn
      {
          class RecordAny;
          class gnuDynAnyFactory;
          class gnuDynStruct;
      }
    }
  }
  namespace org
  {
    namespace omg
    {
      namespace CORBA
      {
          class ORB;
          class TypeCode;
      }
      namespace DynamicAny
      {
          class NameDynAnyPair;
          class NameValuePair;
      }
    }
  }
}

class gnu::CORBA::DynAn::gnuDynStruct : public ::gnu::CORBA::DynAn::RecordAny
{

public:
  gnuDynStruct(::org::omg::CORBA::TypeCode *, ::org::omg::CORBA::TypeCode *, ::gnu::CORBA::DynAn::gnuDynAnyFactory *, ::org::omg::CORBA::ORB *);
public: // actually protected
  virtual ::gnu::CORBA::DynAn::RecordAny * newInstance(::org::omg::CORBA::TypeCode *, ::org::omg::CORBA::TypeCode *, ::gnu::CORBA::DynAn::gnuDynAnyFactory *, ::org::omg::CORBA::ORB *);
public:
  virtual JArray< ::org::omg::DynamicAny::NameDynAnyPair * > * get_members_as_dyn_any();
  virtual JArray< ::org::omg::DynamicAny::NameValuePair * > * get_members();
private:
  static const jlong serialVersionUID = 1LL;
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_CORBA_DynAn_gnuDynStruct__
